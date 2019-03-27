-module(game_handler).
-behavior(cowboy_handler).

-export([init/2]).

init(Req0, State) ->
    Id = binary_to_integer(cowboy_req:binding(id, Req0)),
    [Game|_] = utils:name_fields([id, name, type, geekId], game(Id)),
    Req = cowboy_req:reply(200,
        #{<<"content-type">> => <<"application/json">>},
        jiffy:encode(Game),
        Req0),
    {ok, Req, State}.

game(Id) ->
    {ok, DbPath} = application:get_env(rest_api, dbpath),
    {ok, Db} = esqlite3:open(DbPath),
    Query = io_lib:format("SELECT id, name, type, geek_id FROM bgplays_game WHERE id = ~B;", [Id]),
    esqlite3:q(Query, Db).

