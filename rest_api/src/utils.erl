-module(utils).

-export([name_fields/2]).

name_fields(Fields, Rows) ->
    name_fields(Fields, Rows, []).
name_fields(_, [], Acc) ->
    Acc;
name_fields(Fields, [Row|Rest], Acc) ->
    NewList = [{lists:zip(Fields, tuple_to_list(Row))}|Acc],
    name_fields(Fields, Rest, NewList).

