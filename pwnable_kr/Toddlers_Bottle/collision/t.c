#include <stdio.h>
#include <string.h>

// hashcode = 568134124

unsigned long hashcode = 0x21DD09EC;
char* cmp = "12345678901234567890";

unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
        		printf("ip %d\n", ip[i] );
                res += ip[i];
                printf("%d\n\n",res );
        }
        return res;
}

int main(int argc, char* argv[]){
	
        if(hashcode == check_password( cmp )){
                system("/bin/cat flag");
                return 0;
        }
        else
        {
               // printf("%d\n", check_password( argv[1] ) );
                printf("wrong passcode.\n");
        }
        return 0;
}