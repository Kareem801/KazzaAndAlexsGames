






function single()
{
	room_goto(SignlePlayer);
}


function multi()
{
	room_goto(Multiplayer)
}


function SpawnSingle()
{
	instance_create_depth(0,0,0,oPlayer1); 
}


single = false;
multi = false;