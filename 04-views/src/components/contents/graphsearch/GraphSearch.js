import { useEffect, useState } from 'react';
import withStyles from "@mui/styles/withStyles";
import ButtonGroup from '@mui/material/ButtonGroup';
import Button from '@mui/material/Button';
import Tab from '@mui/material/Tab';
import Tabs from '@mui/material/Tabs';

const styles = (theme) => ({
    wrapper: {
        width: '100%',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center'
    },
    row: {
        listStyle: 'none',
        display: 'flex',
        margin: 0,
        padding: 0
    },
    cell: {
        width: 25,
        height: 25,
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
    buttonGroup: {
        margin: 20
    }
});

const adjacencyPos = [[0, -1], [0, 1], [-1, 0], [1, 0]];
const size = [15, 15];
const initGrid = () => {
    const grid = [];
    const [rowSize, colSize] = size;
    [...Array(rowSize)].forEach(() => {
        const row = [];
        [...Array(colSize)].forEach(() => {
            row.push(0)
        });
        grid.push(row);
    });
    return grid;
};

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

const GraphSearch = (props) => {
    const { classes } = props;
    const [picker, setPicker] = useState(0);
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

    const pickerClickHandler = (e, value) => {
        setPicker(value);
    };

    const cellClickHandler = (row, col) => {
        const newGrid = [...grid];

        let value;
        if (newGrid[row][col] !== 0) value = 0
        if (picker === 0) value = 1;
        if (picker === 1) value = -1;
        if (picker === 2) value = 0;

        newGrid[row][col] = value;
        setGrid(newGrid);
    };

    return (
        <div className={classes.wrapper}>
            <Tabs value={picker} onChange={pickerClickHandler}>
                <Tab label="시작지점" />
                <Tab label="벽" />
                <Tab label="지우기" />
            </Tabs>
            <ButtonGroup className={classes.buttonGroup} variant="outlined">
                <Button onClick={startClickHandler} variant={start ? "contained" : "outlined"}>{start ? '정지' : '시작'}</Button>
                <Button onClick={resetClickHandler}>초기화</Button>
            </ButtonGroup>
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

export default withStyles(styles)(GraphSearch);