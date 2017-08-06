#lang sicp

; implement a procedure that calculates cube roots using Newton's method

(define (cube-root x)
  (define (square x) (* x x))
  (define (cube x) (* x x x))
  (define (try guess)
    (if (good-enough? guess)
        guess
        (try (improve guess))))
  (define (good-enough? guess)
    (< (abs (- (cube guess) x))
       0.001))
  (define (improve guess)
    (/ (+ (/ x
             (square guess))
          (* 2 guess))
       3))
  (try 1.0))

