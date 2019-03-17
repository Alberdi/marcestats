-module(games_handler).
-behavior(cowboy_handler).

-export([init/2]).

init(Req0, State) ->
    Games = name_fields([id, name], game_list()),
    LinkedGames = append_links(Req0, Games),
    Req = cowboy_req:reply(200,
        #{<<"content-type">> => <<"application/json">>},
        jiffy:encode({[{games, LinkedGames}]}),
        Req0),
    {ok, Req, State}.

append_links(Req, Games) ->
    BaseURL = cowboy_req:uri(Req),
    append_links(BaseURL, Games, []).
append_links(_, [], Acc) ->
    Acc;
append_links(BaseURL, [Game|Rest], Acc) ->
    LinkedGame = append_link(BaseURL, Game),
    append_links(BaseURL, Rest, [LinkedGame|Acc]).

append_link(BaseURL, Game) ->
    {append_link(BaseURL, element(1, Game), [])}.
append_link(_, [], Acc) ->
    Acc;
append_link(BaseURL, [{id, Id}|Rest], Acc) ->
    IdString = integer_to_list(Id),
    URL = list_to_binary(lists:flatten(BaseURL ++ ["/", IdString])),
    NewAcc = [{id, Id}|[{url, URL}|Acc]],
    append_link(BaseURL, Rest, NewAcc);
append_link(BaseURL, [H|T], Acc) ->
    append_link(BaseURL, T, [H|Acc]).

game_list() ->
    {ok, DbPath} = application:get_env(rest_api, dbpath),
    {ok, Db} = esqlite3:open(DbPath),
    esqlite3:q("SELECT id, name FROM bgplays_game;", Db).

name_fields(Fields, Rows) ->
    name_fields(Fields, Rows, []).
name_fields(_, [], Acc) ->
    Acc;
name_fields(Fields, [Row|Rest], Acc) ->
    NewList = [{lists:zip(Fields, tuple_to_list(Row))}|Acc],
    name_fields(Fields, Rest, NewList).

