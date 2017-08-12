#lang sicp

(define (even? n) (= (remainder n 2) 0)) ; helpers
(define (halve n) (/ n 2))
(define (double n) (* n 2))

(define (mult a b)
  (define (iter product a b)
    (cond ((= b 0) product)
          ((even? b) (iter product (double a) (halve b)))
          (else (iter (+ product a) a (- b 1)))))
  (iter 0 a b))
