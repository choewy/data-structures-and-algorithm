import { useState } from "react";
import { Route, Routes } from "react-router-dom";
import withStyles from "@mui/styles/withStyles";
import Box from '@mui/material/Box';
import CssBaseline from "@mui/material/CssBaseline";
import NavBar from "./components/commons/NavBar";
import SideBar from "./components/commons/SideBar";
import Paper from "@mui/material/Paper";
import useComponents from "./components/contents/Components";
import Helmets from "./components/commons/Helmets";

const styles = (theme) => ({
  app: {
    width: '100%',
    overflowX: 'hidden'
  },
  components: {
    marginTop: 20,
    paddingBottom: 20,
  }
});

const App = (props) => {
  const { classes } = props;
  const components = useComponents();
  const [open, setOpen] = useState(false);

  const navbarOpenHandler = () => {
    setOpen(true);
  };

  const navbarCloseHandler = () => {
    setOpen(false);
  };

  const navBarProps = {
    open,
    navbarOpenHandler,
  };

  const sideBarProps = {
    open,
    navbarCloseHandler
  };

  return (
    <div className={classes.app}>
      <Helmets />
      <Box sx={{ display: 'flex' }}>
        <CssBaseline />
        <NavBar {...navBarProps} />
        <SideBar {...sideBarProps} />
      </Box>
      <Paper className={classes.components}>
        <Routes>
          {
            components.map((component, key) => {
              const { path, element } = component;
              const componentProps = { key, path, element };
              return <Route {...componentProps} />;
            })
          }
        </Routes>
      </Paper>
    </div>
  );
};

export default withStyles(styles)(App);
