import withStyles from "@mui/styles/withStyles";
import useComponents from "../Components";
import ContentCard from "./ContentCard";

const styles = (theme) => ({
    wrapper: {
        width: '100%',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center'
    },
    menuLink: {
        textDecoration: 'none',
        color: 'inherit'
    }
});

const HomePage = (props) => {
    const { classes } = props;
    const components = useComponents();

    return (
        <div className={classes.wrapper}>
            {
                components.splice(1).map((component, key) => {
                    const { title, to, description, href } = component;
                    const cardProps = { key, title, to, description, href }
                    return (
                        <ContentCard {...cardProps} />
                    )
                })
            }
        </div>
    );
};

export default withStyles(styles)(HomePage);