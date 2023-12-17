sum([], 0).
sum([First|NextEls], Sum) :-
    sum(NextEls, Sum1), Sum is Sum1 + First.

?- sum([2, 7, 10], SumElements), write(SumElements).   