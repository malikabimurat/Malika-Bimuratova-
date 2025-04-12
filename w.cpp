#include <iostream>
#include <algorithm> 
#include <cmath>
#include <vector>
#include <map>
#include <set>
using namespace std;

int main() {
    int q;
    cin>>q;
    map<string,int> m;
    map<string,int> a;
    vector<string> v;
    set<string> t;
    string z,s;
    for(int i=0;i<q;i++){
        cin>>z>>s;
        v.push_back(s);
        m[s]=0;
        a[s]=0;
    }
    for(int i=0;i<q;i++){
        m[v[i]]++;
        t.insert(v[i]);
    }
    int n,k;
    cin>>n;
    
    for(int i=0;i<n;i++){
        cin>>z>>s>>k;
        a[s]+=k;
    }
    set<string>::iterator it;
    int e;
    int r=0;
    for(it=t.begin();it!=t.end();it++){
        e=m[*it]-a[*it];
        if(e>0){
            r+=e;
        }
    }
    cout<<"Bugs left: "<<r;
    



    return 0;
    }