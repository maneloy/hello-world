#lang sicp

; define a procedure that takes 3 arguments and returns
; the sum of the squares of the two larger ones.

(define (procedure x y z)
  (define (square num) (* num num))
  (define (sum-squares a b) (+ (square a) (square b)))
  (define (>= n1 n2) (not (< n1 n2)))
  (cond ((and (>= x z) (>= y z)) (sum-squares x y))
        ((and (>= z y) (>= x y)) (sum-squares x z))
        (else (sum-squares y z))))



