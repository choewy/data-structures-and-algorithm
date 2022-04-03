import GraphSearch from "./graphsearch/GraphSearch";
import HomeIcon from '@mui/icons-material/Home';
import GridOnIcon from '@mui/icons-material/GridOn';
import HomePage from "./homepage/HomePage";

const useComponents = () => {
    return [
        {
            path: '/',
            to: '/',
            label: 'HOME',
            element: <HomePage />,
            icon: <HomeIcon />,
            title: ''
        },
        {
            path: '/1',
            to: '/1',
            label: 'Graph Search',
            element: <GraphSearch />,
            icon: <GridOnIcon />,
            title: '그래프 탐색(DFS/BFS) 알고리즘 구현',
            description: '<백준 7576번 토마토>문제를 풀다가 아이디어를 얻어 알고리즘의 동작 방식을 구현한 컴포넌트',
            href: 'https://www.acmicpc.net/problem/7576'
        }
    ];
};

export default useComponents;