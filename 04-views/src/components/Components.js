import BreadthFirstSearch from "./contents/BreadthFirstSearch";
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
            label: 'BFS',
            element: <BreadthFirstSearch />,
            icon: <GridOnIcon />,
            title: 'BFS 알고리즘 구현',
            description: '<백준 7576번 토마토>문제를 풀고, BFS 알고리즘의 동작 방식을 구현한 컴포넌트',
            href: 'https://www.acmicpc.net/problem/7576'
        }
    ];
};

export default useComponents;