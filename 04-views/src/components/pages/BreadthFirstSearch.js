import { useEffect, useState } from 'react';
import withStyles from "@mui/styles/withStyles";

const styles = (theme) => ({
    wrapper: {},
    row: {
        listStyle: 'none',
        display: 'flex',
        margin: 0
    },
    cell: {
        width: 50,
        height: 50,
        border: '.5px solid #777',
    },
    open: {
        background: '#fff'
    },
    close: {
        background: '#c7ffff'
    },
    wall: {
        background: '#999'
    },
});

const adjacencyPos = [[0, -1], [0, 1], [-1, 0], [1, 0]];

const initGrid = () => [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
];

const initQueue = (initGrid) => {
    const nextCells = [];
    const cellPos = [];
    initGrid.forEach((cells, row) => {
        cells.forEach((cell, col) => {
            if (cell === 1) {
                cellPos.push([row, col]);
            }
        })
    })
    nextCells.push(cellPos);
    return nextCells;
};

const startSearch = (queue, grid) => {
    let nextQueue = [...queue];
    let nextGrid = [...grid];

    const rowCount = grid.length;
    const colCount = grid[0] ? grid[0].length : 0;

    const openPos = nextQueue.pop(0);
    const nextPos = [];

    openPos.forEach(([row, col]) => {
        adjacencyPos.forEach(([nextRow, nextCol]) => {
            const newRow = row + nextRow;
            const newCol = col + nextCol;
            if (newRow < 0 | newRow >= rowCount | newCol < 0 | newCol >= colCount) return;
            if (grid[newRow][newCol] === undefined | grid[newRow][newCol] !== 0) return;
            nextGrid[newRow][newCol] = 1;
            nextPos.push([newRow, newCol]);
        });
    });

    if (nextPos.length > 0) {
        nextQueue.push(nextPos);
    };

    return [nextQueue, nextGrid];
};

const BreadthFirstSearch = (props) => {
    const { classes } = props;
    const [picker, setPicker] = useState('close');
    const [start, setStart] = useState(false);
    const [grid, setGrid] = useState([]);
    const [queue, setQueue] = useState([]);

    useEffect(() => {
        setGrid(initGrid());
        return () => { };
    }, []);

    useEffect(() => {
        if (start) {
            setQueue(initQueue(grid));
        } else {
            setQueue([]);
        };
        return () => { };
    }, [start, grid]);

    useEffect(() => {
        if (queue.length) {
            while (queue.length > 0) {
                const interval = setInterval(() => {
                    const [nextQueue, nextGrid] = startSearch(queue, grid);
                    setQueue(nextQueue);
                    setGrid(nextGrid);
                }, 100);

                return () => {
                    clearInterval(interval);
                };
            };
        } else {
            setStart(false);
        };
    }, [queue, grid]);

    const resetClickHandler = () => {
        setStart(false);
        setGrid(initGrid());
    };

    const startClickHandler = () => {
        setStart(!start);
    };

    const pickerClickHandler = (e) => {
        const { target: { name } } = e;
        setPicker(name);
    };

    const cellClickHandler = (row, col) => {
        const newGrid = [...grid];
        if (picker === "open") {
            newGrid[row][col] = 0;
        };
        if (picker === "close") {
            newGrid[row][col] = 1;
        };
        if (picker === "wall") {
            newGrid[row][col] = -1;
        };
        setGrid(newGrid);
    };

    return (
        <div className={classes.wrapper}>
            <div>
                <button onClick={startClickHandler}>{start ? 'Stop' : 'Start'}</button>
                <button onClick={resetClickHandler}>{'Reset'}</button>
            </div>
            <div>
                <button name="close" onClick={pickerClickHandler}>Start Point</button>
                <button name="wall" onClick={pickerClickHandler}>Wall</button>
                <button name="open" onClick={pickerClickHandler}>Clear</button>
            </div>
            {
                grid.map((values, row) => {
                    const rowProps = {
                        key: row,
                        className: classes.row
                    };
                    return (
                        <ul {...rowProps}>
                            {
                                values.map((value, col) => {
                                    const cellProps = {
                                        key: `${row}-${col}`,
                                        className: classes.cell,
                                        onClick: () => cellClickHandler(row, col)
                                    };

                                    if (value === 0) {
                                        cellProps.className += ` ${classes.open}`
                                    };

                                    if (value === 1) {
                                        cellProps.className += ` ${classes.close}`
                                    };

                                    if (value === -1) {
                                        cellProps.className += ` ${classes.wall}`
                                    };

                                    return <li {...cellProps} />;

                                })
                            }
                        </ul>
                    );
                })
            }
        </div>
    );
};

export default withStyles(styles)(BreadthFirstSearch);