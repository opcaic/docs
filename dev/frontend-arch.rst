################################
 Web app architecture
################################

dsad

*******************
 React boilerplate
*******************

The core of the whole application comes from the `react boilerplate <https://github.com/react-boilerplate/react-boilerplate>`_ project where you can find how to use individual libraries included in the project and also the motivation for why to use them. Our application does not strictly follow all the patterns introduced in the boilerplate project.

**************************
 Most important libraries
**************************

- `React <https://reactjs.org/>`_ - UI framework
- `Ant Design <https://github.com/ant-design/ant-design>`_ - components for building the UI
- `Redux <https://redux.js.org/>`_ - state management
- `Redux-Saga <https://github.com/redux-saga/redux-saga>`_ - asynchronous data loading
- `React Router <https://github.com/ReactTraining/react-router>`_ - routing
- `React Intl <https://github.com/formatjs/react-intl>`_ - localization

**************************
 Application structure
**************************

**************************
 Module structure
**************************

- *components* - React components
- *containers* - React containers
- *ducks* - handling store updates, api calls..
- *pages* - indvidual web pages of the module
- *selectors* (optional) - store selectors
- *utils* (optional) - utility functions
- *PublicApp*/*AdminApp* component - entry point of the module

Components and containers
=========================

In the React ecosystem, we often distinguish between *(presentational) components* and *containers*. *Components* are concerned with *how things look*, while *containers*

.. todo:: TODO