import withStyles from "@mui/styles/withStyles";
import { Route, Routes } from "react-router-dom";
import PageIndex from "./components/commons/PageIndex";
import BreadthFirstSearch from "./components/pages/BreadthFirstSearch";

const styles = (theme) => ({
  app: {
    width: '100%',
    marginTop: theme.spacing.unit * 3,
    overflowX: 'auto'
  },
});

const App = () => {
  return (
    <div className="app">
      <PageIndex />
      <Routes>
        <Route path="/1" element={<BreadthFirstSearch />} />
      </Routes>
    </div>
  );
};

export default withStyles(styles)(App);
