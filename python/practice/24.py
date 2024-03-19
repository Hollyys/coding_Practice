def solution(id_list, report, k):
    answer = []
    index_list = {}
    receive_list = {}
    
    for idx in range(len(id_list)):
        answer.append(0)
        index_list[id_list[idx]] = idx
    
    for data in report:
        sender = data.split()[0]
        receiver = data.split()[1]    
        if receiver in receive_list and sender not in receive_list[receiver]:
            receive_list[receiver].append(sender)
        elif receiver not in receive_list:
            receive_list[receiver] = [sender]
            
    for name in receive_list:
        if len(receive_list[name]) >= k:
            for mail in receive_list[name]:
                answer[index_list[mail]] += 1
        
    # print(send_list, receive_list)
    return answer

# #include <stdio.h>
# #include <stdbool.h>
# #include <stdlib.h>
# #include <string.h>

# int* solution(const char* id_list[], size_t id_list_len, const char* report[], size_t report_len, int k) {
#     // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.

#     //init
#     int tmp[id_list_len][id_list_len];
#     for(int i = 0; i<id_list_len; ++i)
#     {
#         for(int j =  0; j<id_list_len; ++j)
#         {
#             tmp[i][j] = 0;
#         }
#     }

#     for(int i = 0; i<report_len; ++i)
#     {
#         char* pch;
#         pch = strtok (report[i]," ");

#         int idx1 = 0;
#         for(int j = 0; j<id_list_len; ++j)
#         {
#             if(strcmp(id_list[j],pch) == 0)
#             {
#                 idx1 = j;
#             }
#         }
#         pch = strtok(NULL, " ");
#         int idx2 = 0;
#         for(int j = 0; j<id_list_len; ++j)
#         {
#             if(strcmp(id_list[j],pch) == 0)
#             {
#                 idx2 = j;
#             }
#         }

#         tmp[idx1][idx2] += 1;        
#     }

#     int tmp2[id_list_len];
#     for(int i = 0; i<id_list_len; ++i)
#     {
#         tmp2[i] = 0;
#         for(int j =  0; j<id_list_len; ++j)
#         {
#             if(tmp[j][i] > 0)
#             {
#                 tmp2[i] += 1;
#             }
#         }
#     }

#     int* answer = (int*)malloc(id_list_len*sizeof(int));
#     for(int i = 0; i<id_list_len; ++i)
#     {
#         answer[i] = 0;
#         for(int j =  0; j<id_list_len; ++j)
#         {
#             if(tmp[i][j] > 0 && tmp2[j] >= k)
#             {
#                 answer[i] += 1;
#             }
#         }
#     }



#     return answer;

# }

# /*
# // id_list_len은 배열 id_list의 길이입니다.
# // report_len은 배열 report의 길이입니다.
# // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
# int* solution(const char* id_list[], size_t id_list_len, const char* report[], size_t report_len, int k) {
#     // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
#     int i,j;
#     int* answer = (int*)malloc(id_list_len);
#     int* banned = (int*)malloc(id_list_len);
#     int* flag = (int*)malloc(report_len);
#     for(i=0; i<id_list_len; i++){
#         answer[i] = 0;
#         banned[i] = 0;
#     }
#     for(i=0; i<report_len; i++){
#         flag[i] = 1;
#         for(j=i+1; j<report_len; j++){
#             if(strcmp(report[i], report[j])==0)
#                 flag[i] = 0;
#         }
#     }
    
#     char* buffer = (char*)malloc(sizeof(char)*21);    
#     for(i=0; i<report_len; i++){
#         if(flag[i] == 1){
#             strcpy(buffer, report[i]);
#             char *buf = strtok(buffer, " ");
#             buf = strtok(NULL, " ");
#             printf("%s ", buf);
            
#             for(j=0; j<id_list_len; j++){
#                 if(strcmp(id_list[j], buf) == 0)
#                     ++banned[j];
#             }
#         }
#     }
    
#     for(i=0; i<report_len; i++){
#         char* a = (char*)malloc(10);
#         int add_a;
#         char* b = (char*)malloc(10);
#         int add_b;
        
#         if(flag[i] == 1){
#             char *buf = strtok(report[i], " ");
#             strcpy(a, buf);
#             buf = strtok(NULL, " ");
#             strcpy(b, buf);
            
#             for(j=0; j<id_list_len; j++){
#                 if(strcmp(id_list[j], a) == 0)
#                     add_a = j;
#                 if(strcmp(id_list[j], b) == 0)
#                     add_b = j;
#             }
            
#             if(banned[add_b] >= k)
#                 ++answer[add_a];
#         }
#     }
    
#     return answer;
# }*/