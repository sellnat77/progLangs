(defn coord[] (list (rand) (rand)))
(defn is-hit? [d] (>= 1 (+ (* (first d) (first d)) (* (second d) (second d)))))
(defn throw-darts [n] (take n (repeatedly coord)))
(defn count-hits [n] (count (filter #(is-hit? %) (throw-darts n))))
(defn estimate-pi [n] (* 4 (/ (count-hits n) (double n))))

(defn readFile [file]
  (take 10 (sort-by last >
             (frequencies
               (re-seq #"[a-zA-Z]+"
                 (clojure.string/lower-case
                   (slurp file)
                   )
                 )
               )
             )
    )
  )

(defn myFlatten [coll]
  (if (empty? coll)
    nil
    (if (list? (first coll))
      (concat
        (myFlatten (first coll))
        (myFlatten (next coll))
        )
      (cons
        (first coll)
        (myFlatten (next coll))
        )
      )
    )
  )

