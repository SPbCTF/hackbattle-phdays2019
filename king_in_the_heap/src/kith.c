#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

typedef struct{
    char password[32];
    char name[32];
    unsigned int age;
    char meta[256];
} User;

unsigned char marker = 0;

void purify(char* s){
    int i = 0;
    while(s[i]!='\n' && s[i]!='\x00')
        i++;
    s[i]='\x00';
}


int main(int argc, char** argv){

    User* user = (User*) malloc (sizeof(User));
    User* admin = (User*) malloc (sizeof(User));

    strcpy(admin->name, "Shtrikh17");
    admin->age = 23;
    strcpy(admin->password, "admin");
    strcpy(admin->meta, "flag{no_flag_offline}");

    puts("Welcome to the king in the heap contest.\nAre you ready to become an admin?");
    puts("Commands:");
    puts("* exit - exit the program");
    puts("* login - login");
    puts("* meta - get current meta");
    fflush(stdout);

    char command[32];

    while(1){
        printf("> ");
        fflush(stdout);
        fgets(command, 32, stdin);
        purify(command);
        if(!strcmp(command, "exit")){
            break;
        }
        else if(!strcmp(command, "login")){
            char login[32];
            char password[32];
            printf("Login: ");
            fflush(stdout);
            fgets(login,33,stdin);
            purify(login);
            printf("Password: ");
            fflush(stdout);
            fgets(password,33,stdin);
            purify(password);
            if(!strcmp(login, admin->name)){
                if(!strcmp(password, admin->password)){
                    marker = 2;
                }
                else{
                    puts("Wrong password");
                }
            }
            else{
                strcpy(user->name, login);
                strcpy(user->password, password);
                marker = 1;
                printf("Age: ");
                fflush(stdout);
                scanf("%d", &(user->age));
                printf("Meta: ");
                fflush(stdout);
                scanf("%s", user->meta);
                getc(stdin);
            }
        }
        else if(!strcmp(command, "meta")){
            if(marker==1){
                printf("Name: %s\n", user->name);
                printf("Password: %s\n", user->password);
                printf("Age: %d\n", user->age);
                printf("Meta: %s\n", user->meta);
            }
            else if(marker==2){
                printf("Name: %s\n", admin->name);
                printf("Password: %s\n", admin->password);
                printf("Age: %d\n", admin->age);
                printf("Meta: %s\n", admin->meta);
            }
            else{
                puts("No meta for you");
            }
        }
        else{
            puts("Wrong command!");
        }
        fflush(stdout);
    }
    puts("Bye!");
    

    return 0;
}