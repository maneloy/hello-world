#lang sicp

(define (f1 n)  ; recursive
  (if (< n 3)
      n
      (+ (f1 (- n 1))
         (* (f1 (- n 2)) 2)
         (* (f1 (- n 3)) 3))))

(define (f2 n)  ; iterative
  (define (f-iter a b c count)
    (if (= count 0)
        c
        (f-iter (+ a (* 2 b) (* 3 c)) a b (- count 1))))
  (f-iter 2 1 0 n))