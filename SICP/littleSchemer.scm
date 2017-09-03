#lang scheme

;; ~~~LAWS~~~
;; Law of Car: The primitive 'car' is defined only for non-empty lists.
;; Law of Cdr: The primitive 'cdr' is efined only for non-empty lists. The cdr of any non-empty list is always another list.
;; Law of Cons: The primitive 'cons' takes two arguments. The second must be a list. The result is a list.
;; Law of Null?: The primitive 'null?' is defined only for lists.
;; Law of Eq?: The primitive 'eq?' takes two arguments. Each must be a non-numeric atom.

;; ~~~COMMANDMENTS~~~
;; First Commandment: Always ask 'null?' as the first question in expressing any function.
;; Second Commandment: Use 'cons' to build lists.
;; Third Commandment: When building a list, describe the first typical element, and the cons it onto the natural recursion.

(define atom? ;; strings of characters not enclosed by ()
  (lambda (x)
    (and (not (pair? x))
         (not (null? x)))))

(define lat? ;; lists whose individual members are all atoms
  (lambda (l)
    (cond
      ((null? l) true)
      ((atom? (car l)) (lat? (cdr l)))
      (else false))))

(define member? ;; is the atom 'a' a member of the list of atoms 'lat'?
  (lambda (a lat)
    (cond
      ((null? lat) false)
      (else (or (eq? (car lat) a)
                (member? a (cdr lat)))))))

(define rember  ;; remove first ocurrence of 'a' in 'lat'.
  (lambda (a lat)
    (cond
      ((null? lat) (quote ()))
      ((eq? (car lat) a) (cdr lat))
      (else (cons (car lat)
                  (rember a (cdr lat)))))))

(define firsts     ;; Takes a list of non-empty lists (or a null list) and 
  (lambda (l)      ;; returns a list with the first S-exp of each list.
    (cond
      ((null? l) (quote ()))
      (else (cons (car (car l))
                  (firsts (cdr l)))))))

(define seconds    ;; Takes a list of non-empty lists (or a null list) and 
  (lambda (l)      ;; returns a list with the second S-exp of each list.
    (cond
      ((null? l) (quote ()))
      (else (cons (car (cdr (car l)))
                  (seconds (cdr l)))))))
