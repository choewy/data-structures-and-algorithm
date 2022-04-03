import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import withStyles from "@mui/styles/withStyles";
import { Link } from 'react-router-dom';

const styles = (theme) => ({
    card: {
        maxWidth: 500,
        minWidth: 300,
        margin: 10
    },
    link: {
        textDecoration: 'none',
        color: 'inherit'
    }
});

const ContentCard = (props) => {
    const { classes, title, to, description, href } = props;

    const linkProps = {
        to,
        className: classes.link
    };

    const aProps = {
        href,
        target: '_blank',
        rel: 'noreferrer',
        className: classes.link
    };

    return (
        <Card className={classes.card}>
            {/* <CardMedia
                component="img"
                alt="green iguana"
                height="140"
                image="/static/images/cards/contemplative-reptile.jpg"
            /> */}
            <CardContent>
                <Typography gutterBottom variant="h5" component="div">
                    {title}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    {description}
                </Typography>
            </CardContent>
            <CardActions>
                <Link {...linkProps}><Button size="small">자세히</Button></Link>
                <a {...aProps}><Button size="small">문제보기</Button></a>
                {/* <Button size="small">공유하기</Button> */}
            </CardActions>
        </Card>
    );
};

export default withStyles(styles)(ContentCard);