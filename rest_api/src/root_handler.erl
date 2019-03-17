-module(root_handler).
-behavior(cowboy_handler).

-export([init/2]).

init(Req0, State) ->
    Links = generate_links(Req0),
    Req = cowboy_req:reply(200,
        #{<<"content-type">> => <<"application/json">>},
        jiffy:encode({Links}),
        Req0),
    {ok, Req, State}.

generate_links(Req) ->
    BaseURL = cowboy_req:uri(Req),
    Games = list_to_binary(lists:flatten(BaseURL ++ "games")),
    [{games, Games}].
