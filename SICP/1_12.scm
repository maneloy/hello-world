#lang sicp

(define (pascal row column)   ; pascal's triangle
  (if (or (= row 0) (= column 0) (= row column))
      1
      (+ (pascal (- row 1) column)
         (pascal (- row 1) (- column 1)))))