import { createRef, useEffect } from "react";
import withStyles from "@mui/styles/withStyles";

const styles = () => ({
    comments: {
        marginTop: 50
    }
});

const Utteranc = (props) => {
    const { classes } = props;
    const commentRef = createRef();

    useEffect(() => {
        const isExist = commentRef.current.firstChild;

        if (isExist) return () => { };

        const utteranc = document.createElement('script');
        const utterancConfig = {
            src: 'https://utteranc.es/client.js',
            repo: 'choewy/data-structures-and-algorithm',
            theme: 'github-light',
            "issue-term": "pathname",
            async: true,
            crossorigin: "anonymous"
        };

        Object.entries(utterancConfig).forEach(([key, value]) => {
            utteranc.setAttribute(key, value);
        });

        commentRef.current.appendChild(utteranc);

        return () => { };
    }, [commentRef]);

    return <div className={classes.comments} ref={commentRef} />
};

export default withStyles(styles)(Utteranc);