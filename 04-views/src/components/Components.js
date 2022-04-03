import BreadthFirstSearch from "./contents/BreadthFirstSearch";
import HomeIcon from '@mui/icons-material/Home';
import GridOnIcon from '@mui/icons-material/GridOn';
import HomePage from "./contents/HomePage";

const useComponents = () => {
    return [
        {
            path: '/',
            to: '/',
            label: 'HOME',
            element: <HomePage />,
            icon: <HomeIcon />
        },
        {
            path: '/1',
            to: '/1',
            label: 'BFS',
            element: <BreadthFirstSearch />,
            icon: <GridOnIcon />
        }
    ];
};

export default useComponents;