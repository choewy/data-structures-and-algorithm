import withStyles from "@mui/styles/withStyles";
import IconButton from '@mui/material/IconButton';
import Drawer from "@mui/material/Drawer";
import { useTheme } from "@emotion/react";
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import Divider from '@mui/material/Divider';
import SideContentMenus from "./SideContentMenus";
import SideMainMenus from "./SideMainMenus";

const styles = (theme) => ({
    drawer: {
        width: drawerWidth,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
            width: drawerWidth,
            boxSizing: 'border-box',
        },
    },
    drawerHeader: {
        display: 'flex',
        alignItems: 'center',
        padding: theme.spacing(0, 1),
        ...theme.mixins.toolbar,
        justifyContent: 'flex-end',
    }
});

const drawerWidth = 240;

const SideBar = (props) => {
    const theme = useTheme();
    const { classes, open, navbarCloseHandler } = props;

    return (
        <Drawer
            className={classes.drawer}
            variant="persistent"
            anchor="left"
            open={open}>
            <div className={classes.drawerHeader}>
                <IconButton onClick={navbarCloseHandler}>
                    {theme.direction === 'ltr' ? <ChevronRightIcon /> : <ChevronLeftIcon />}
                </IconButton>
            </div>
            <Divider />
            <SideMainMenus />
            <Divider />
            <SideContentMenus navbarCloseHandler={navbarCloseHandler} />
        </Drawer>
    );
};

export default withStyles(styles)(SideBar);