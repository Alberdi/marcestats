-module(rest_api_app).
-behaviour(application).

-export([start/2]).
-export([stop/1]).

start(_Type, _Args) ->
    Dispatch = cowboy_router:compile([
        {'_', [{"/", root_handler, []},
               {"/games", games_handler, []},
               {"/games/:id", game_handler, []}
              ]}
    ]),
    {ok, _} = cowboy:start_clear(my_http_listener,
        [{port, 8080}],
        #{env => #{dispatch => Dispatch}}
    ),
    rest_api_sup:start_link().

stop(_State) ->
    ok.
