#lang sicp

(define (expt b n) ; recursive, straightforward
  (if (= n 0)
      1
      (* b (expt b (- n 1)))))

(define (faster-expt b n) ; iterative, straightforward
  (define (expt-iter product count)
    (if (or (= count 0) (< count 0))
        product
        (expt-iter (* product b) (- count 1))))
  (expt-iter 1 n))

(define (square x) (* x x)) ; helpers
(define (even? num)
    (= (remainder num 2) 0))

(define (fast-expt b n) ; recursive, uses successive squaring
  (cond ((= n 0) 1)
        ((even? n) (square (fast-expt b (/ n 2))))
        (else (* b (fast-expt b (- n 1))))))

(define (fastest-expt b n) ; iterative, uses successive squaring. Exercise 1.16
  (define (fast-expt-iter a count)
    (if (or (= count 1) (< count 1))
        a
        (fast-expt-iter (square a) (/ count 2))))
  (if (even? n)
      (fast-expt-iter b n)
      (* b (fast-expt-iter b (- n 1)))))
