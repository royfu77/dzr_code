-module(mgeebgp_sup).

-behaviour(supervisor).

-include("common.hrl").

-export([start_link/0]).

-export([
	 init/1
        ]).

-define(SERVER, ?MODULE).

%% --------------------------------------------------------------------

start_link() ->
	supervisor:start_link({local, ?SERVER}, ?MODULE, []).

init([]) ->
    {ok,{{one_for_one,10,10}, []}}.

%% --------------------------------------------------------------------
