;;; hello-world.el --- Description -*- lexical-binding: t; -*-
;;
;; Copyright (C) 2021 pythonicqualms
;;
;; Author: pythonicqualms <https://github.com/discepati>
;; Maintainer: pythonicqualms <pythonicqualms@gmail.com>
;; Created: July 31, 2021
;; Modified: July 31, 2021
;; Version: 0.0.1
;; Package-Requires: ((emacs "24.3"))
;;
;; This file is not part of GNU Emacs.

;;; Commentary:
;;
;;  Description
;;
;;; Code:

(defun helloWorld ()
  "Just say hello."
  (interactive)
  "Hello, world")

(helloWorld)

(let ((birch 3)
      pine
      fir)
  (message "some things %s"
           birch))

(let (derpen 'derp)
  (message "thing: %s."
           derp))
(current-buffer)
(provide 'hello-world)

(defun simplified-end-of-buffer ()
  "Move point to end of buffer."
  (interactive)
  (push-mark)
  (goto-char (point-max)))

(defun simplified-get-buffer-by-name (buffer-name)
  "The name of the BUFFER-NAME to get."
  (interactive "b")
  (get-buffer buffer-name))

(defun simplified-get-buffer-by-name2 (buffer-name)
  "The name of the BUFFER-NAME to get."
  (let ((mybuf (get-buffer buffer-name)))
    (if (equal mybuf nil)
        (message "Buffer doesnt exist: %s." buffer-name))))

(simplified-get-buffer-by-name2 "*Messages*")

(let ((thing1 'thang2)
      (thing2 'thing2))
  (message "things are: %s and %s." thing1 thing2))


(let (my-buffer (get-buffer "*Messages*")))

(let ((mybuf (get-buffer "*Messages*")))
  (message "buffer is: %s" mybuf))

(find-tag "copy-to-buffer")
(get-buffer "*Messages*")

(mapcar #'bufferp (list "*Messages*" (get-buffer "*Messages*")))

(list "*Messages*" (get-buffer "*Messages*"))

;; Write an interactive function with an optional argument that
;; tests whether its argument, a number, is greater or less than
;; the value of fill-column, and tells you which, in a message.
;; However, if you do not pass an argument to the function, use
;; 56 as a default value.

(defun test-fill-column (&optional arg)
  "Testing 'fill-column' with optional ARG."
  (if arg
      (if (> arg fill-column)
          (message "arg: %d is greater than fill-column %d" arg fill-column)
        (message "arg: %d is less than fill-column %d" arg fill-column))
    (let ((arg 56)) (message "arg is %d" arg))))

(test-fill-column)

(defun what-line ()
  "Print the current line number at point."
  (interactive)
  (save-restriction
    (widen)
    (save-excursion
      (beginning-of-line)
      (message "Line %d"
               (1+ (count-lines 1 (point)))))))

(what-line)
;; display first 60 chars of current buffer
(defun display-first-60-of-buffer ()
  "Print the first 60 lines of the current buffer."
  (interactive)
  (save-restriction
    (widen)
    (save-excursion
      (goto-char (point-min))
      (let
          ((buf-contents (buffer-substring (point-min) 60)))
        (message "buf contents: %s" buf-contents)))))


(let
    ((buf-contents (buffer-substring (point-min) 60)))
  (message "%s" buf-contents))
(display-first-60-of-buffer)
(goto-char (point-min))


(let
    ((my-list '(derp derpen derpenstein)))
  (message "%s" my-list))

(let ((my-bird-list (cons (cons (cons "hawk" "falcon")
            "eagle")
                          "sparrow")))
  (message "tha birds: %s" my-bird-list))
(cons (cons (cons "hawk" "falcon")
            "eagle")
      "sparrow")

(cons (cons (list 'hawk 'falcon) 'eagle) 'pigeon)

(defun jd/count-words-buffer ()
  "Count words in current buffer."
  (let ((count 0))
    (save-excursion
      (goto-char (point-min))
      (while (< (point) (point-max))
        (forward-word 1)
        (setq count (1+ count)))
      (message "buffer contains %d words" count))))

(defun jd/count-lines-buffer ()
  "Count lines in current buffer."
  (let ((count 0))
    (save-excursion
      (goto-char (point-min))
      (while (< (point) (point-max))
        (forward-line 1)
        (setq count (1+ count)))
      (message "buffer contains %d lines" count))))

(defun jd/count-chars-buffer ()
  "Count lines in current buffer."
  (let ((count 0))
    (save-excursion
      (goto-char (point-min))
      (while (< (point) (point-max))
        (forward-char 1)
        (setq count (1+ count)))
      (message "buffer contains %d chars" count))))

(count-words-buffer)
(jd/count-lines-buffer)
(jd/count-chars-buffer)
;;; hello-world.el ends here and here
