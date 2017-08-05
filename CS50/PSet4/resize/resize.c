/**
 * Resizes a BMP image by a factor.
 */
       
#include <stdio.h>
#include <stdlib.h>
#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize factor infile outfile\n");
        return 1;
    }

    // remember filenames
    float factor = strtof(argv[1], NULL);
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file 
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf, nbf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);
    nbf = bf;
    
    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi, nbi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);
    nbi = bi;
    
    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || 
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // update dimensions
    nbi.biWidth = bi.biWidth * factor;
    nbi.biHeight = bi.biHeight * factor;
    
    // determine old and new padding;
    int old_padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    int new_padding = (4 - (nbi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4; 
    
    // update sizes
    nbi.biSizeImage = ((sizeof(RGBTRIPLE) * bi.biWidth) + new_padding) * abs(bi.biHeight);
    nbf.bfSize = bf.bfSize - bi.biSizeImage + nbi.biSizeImage;

    // write outfile's BITMAPFILEHEADER
    fwrite(&nbf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&nbi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        // iterate over scanline factor times
        for (int j = 0; j < factor; j++) {
            // iterate over pixels in scanline
            for (int k = 0; k < bi.biWidth; k++)
            {
                // temporary storage
                RGBTRIPLE triple;

                // read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
                
                // write RGB triple to outfile factor times
                for (int l = 0; l < factor; l++)
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);   
            }
            // add padding
            for (int m = 0; m < new_padding; m++)
                fputc(0x00, outptr);
                
            // return to star of scanline
            if (j < factor - 1)
                fseek(inptr, -bi.biWidth * sizeof(RGBTRIPLE), SEEK_CUR);
        }
                    
        // skip over padding, if any
        fseek(inptr, old_padding, SEEK_CUR);
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
