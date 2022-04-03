import withStyles from "@mui/styles/withStyles";
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import GitHubIcon from '@mui/icons-material/GitHub';
import WebIcon from '@mui/icons-material/Web';

const styles = (theme) => ({
    a: {
        textDecoration: 'none',
        color: 'inherit'
    }
});

const mainMenuItems = [
    {
        href: 'https://github.com/choewy/data-structures-and-algorithm',
        label: 'GitHub',
        icon: <GitHubIcon />
    },
    {
        href: 'https://choewy.tistory.com',
        label: 'Blog',
        icon: <WebIcon />
    },
];

const SideMainMenus = (props) => {
    const { classes } = props;

    return (
        <List>
            {mainMenuItems.map((menuItem, key) => {
                const { href, label, icon } = menuItem;
                const aProps = {
                    key, href,
                    target: '_blank',
                    className: classes.a
                };
                return (
                    <a {...aProps}>
                        <ListItem button>
                            <ListItemIcon>
                                {icon}
                            </ListItemIcon>
                            <ListItemText primary={label} />
                        </ListItem>
                    </a>
                )
            })}
        </List>
    );
};

export default withStyles(styles)(SideMainMenus);