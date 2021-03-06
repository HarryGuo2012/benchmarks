#include <bits/stdc++.h>

std::vector<int> vertexList;
std::vector<std::pair<int, int> > edgeList;

char buff[256];

int main(int argc, char *argv[]) {
    std::ifstream ifs(argv[1]);

    int cnt = 0;

    while (ifs.getline(buff, 256)) {
        cnt = cnt + 1;
        if (cnt == 1) continue;

        int u, v;
        std::stringstream ss;
        ss << buff;
        ss >> u >> v;

        if (u == v) continue;

        vertexList.push_back(u);
        vertexList.push_back(v);

        if (u > v) std::swap(u, v);

        edgeList.push_back(std::make_pair(u, v));
    }

    std::sort(vertexList.begin(), vertexList.end());
    auto it = std::unique(vertexList.begin(), vertexList.end());
    vertexList.resize(std::distance(vertexList.begin(), it));

    for (auto &e : edgeList) {
        int &u = e.first;
        int &v = e.second;

        u = std::lower_bound(vertexList.begin(), vertexList.end(), u) - vertexList.begin() + 1;
        v = std::lower_bound(vertexList.begin(), vertexList.end(), v) - vertexList.begin() + 1;
    }

    std::sort(edgeList.begin(), edgeList.end());
    auto jt = std::unique(edgeList.begin(), edgeList.end());
    edgeList.resize(std::distance(edgeList.begin(), jt));

    int n = vertexList.size();
    int m = edgeList.size();

    std::ofstream ofs(argv[2]);

    ofs << n << " " << m << std::endl;
    for (auto e : edgeList) ofs << e.first << " " << e.second << std::endl;
    return 0;
}