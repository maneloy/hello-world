/**********************************
 * Reads through a memory card    *
 * and looks for possible         *
 * jpeg files, as well as placing *
 * them in the same folder.       *
 **********************************/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCKSIZE 512
#define RAWSIZE 12000000
    
void add_extension(char *name, char *extension);

int main(int argc, char *argv[]) {

    if (argc !=  2) {
        fprintf(stderr, "Usage: ./recover <image>\n");
        return 1;
    }
    
    char *infile = argv[1];
    char outfile[30] = "1.jpeg";
    char extension[10] = ".jpeg";
    int count = 1;
    
    FILE *card = fopen(infile, "r");
    
    if (card == NULL) {
        fclose(card);
        printf("Could not open %s\n", argv[1]);
        return 2;
    }
    
    uint8_t block[BLOCKSIZE];
    FILE *image = fopen(outfile, "w");
    fread(&block, 1, BLOCKSIZE, card);
    
    uint8_t byte = 0x00;
    while (byte != 0xff)
        fread(&byte, 1, 1, card);
    fseek(card, -1, SEEK_CUR);
    fread(&block, 1, BLOCKSIZE, card);
    fwrite(&block, 1, BLOCKSIZE, image);
    
    for (int i = 0; i < (RAWSIZE / BLOCKSIZE); i++) {
        
        fread(&block, 1, BLOCKSIZE, card);
        
        if (block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && (block[3] >= 0xe0 && block[3] <= 0xef)) {
            fclose(image);
            count++;
            snprintf(outfile, 4, "%d", count);
            add_extension(outfile, extension);
            FILE *image = fopen(outfile, "w");
            fwrite(&block, 1, BLOCKSIZE, image);
        } else {
            fwrite(&block, 1, BLOCKSIZE, image);
        }
    }
        
    return 0;            
}

void add_extension(char *name, char *extension) {
    int i, j;
    i = 0;
    j = 0;
    while (name[i] != '\0')
        i++;
    while (extension[j] != '\0')
        name[i++] = extension[j++];
    name[i] = '\0';
}
