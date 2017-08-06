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

; added the sqrt rocedure explained in the book, just because :)

(define (sqrt x)
  (define (square x) (* x x))
  (define (average x y)
    (/ (+ x y) 2))
  (define (good-enough? guess x)
    (< (abs (- (square guess) x)) 0.001))
  (define (improve guess x)
    (average guess (/ x guess)))
  (define (sqrt-iter guess x)
    (if (good-enough? guess x)
        guess
        (sqrt-iter (improve guess x) x)))
  (sqrt-iter 1.0 x))


        