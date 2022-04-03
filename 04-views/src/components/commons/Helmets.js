import { Helmet } from "react-helmet-async"

const meta = {
    title: 'Algorithm Viewes | CHOEWY',
    description: '공부한 알고리즘을 복습하기 위해 만들어본 웹 페이지',
    image: '%PUBLIC_URL%/logo.png',
    url: 'https://choewy.github.io/data-structures-and-algorithm'
};

const Helmets = () => {
    return (
        <Helmet>
            <meta property="og:type" content="website" />
            <meta property="og:title" content={meta.title} />
            <meta property="og:site_name" content={meta.title} />
            <meta property="og:description" content={meta.description} />
            <meta property="og:image" content={meta.image} />
            <meta property="og:url" content={meta.url} />
            <title>{meta.title}</title>
        </Helmet>
    );
};

export default Helmets;