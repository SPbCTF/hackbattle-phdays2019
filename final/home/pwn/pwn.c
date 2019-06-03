#include <stdio.h>

int work(){
 char buf1[64];
 puts("Welcome to shmel-panel");
 fflush(stdout);
 while(1){
     gets(buf1);
     if (!strcmp(buf1,"launch")){
         puts("Enter shmel name");
         fflush(stdout);
         gets(buf1);
         printf("Shmel ");
         printf(buf1);
         printf(" launched\n");
         fflush(stdout);
     }
     else if (!strcmp(buf1,"catch")){
         puts("Enter shmel name");
         fflush(stdout);
         gets(buf1);
         printf("Shmel %s caught\n", buf1);
         fflush(stdout);
     }
     else{
      break;   
     }
 }   
}

int main (){
 work();
 return 0;
}
