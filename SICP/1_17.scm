#lang sicp

(define (even? n) (= (remainder n 2) 0)) ; helpers
(define (halve n) (/ n 2))
(define (double n) (* n 2))

(define (log-mult a b)                   ; recursive logarithmic mult function
  (cond ((= b 0) 0)
        ((even? b) (double (log-mult a (halve b))))
        (else (+ a (log-mult a (- b 1))))))

