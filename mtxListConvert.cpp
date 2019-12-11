#include <bits/stdc++.h>

char buff[256];

int n, m;

int main(int argc, char *argv[]) {
    std::ifstream ifs(argv[1]);
    std::ofstream ofs(argv[2]);

    int cnt = 0;

    while (ifs.getline(buff, 256)) {
        if (buff[0] == '%') continue;

        cnt = cnt + 1;

        std::stringstream ss;
        ss << buff;

        if (cnt == 1) {
            int t;
            ss >> t >> n >> m;
            ofs << n << " " << m << std::endl;
            continue;
        }

        int u, v;
        ss >> u >> v;
        ofs << u << " " << v << std::endl;
        
    }
    return 0;
}