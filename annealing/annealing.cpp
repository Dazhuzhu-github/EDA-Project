#include <iostream>
#include <stdio.h>
#include <cstring>
#include <vector>
using namespace std;

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