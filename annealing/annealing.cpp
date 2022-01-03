#include <iostream>
#include <stdio.h>
#include <cstring>
#include <vector>
using namespace std;

// inline int readNum() // 快速读入
// {
//     char ch = getchar();
//     while (ch < '0' || ch > '9') ch = getchar();
//     int v = 0;
//     while (ch >= '0' && ch <= '9') {
//         v = v * 10 + ch - '0';
//         ch = getchar();
//     }
//     return v;
// };
int main()
{
    freopen("data.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int L; //area length
    int W; //area width
    int M; //number of cell
    int N; //number of net
    cin>>L;
    cin>>W; 
    cin>>M;
    cin>>N;
    vector<vector<int>> net(N);
    getchar();
    getchar();
    int a;

    for(int i = 0;i < N; i++){
        cin>>a;
        cout<<a;
        net[i].push_back(a);
        while (cin.get() != '\n') 
        {
            cin >> a;
            net[i].push_back(a);
        }
        cout<<"\n";
    }
    return 0;
}