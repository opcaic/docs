################################
 Web app architecture
################################

The web application is a single-page app built using the `React <https://reactjs.org/>`_ library.

*******************
 React boilerplate
*******************

The core of the whole application comes from the `react boilerplate <https://github.com/react-boilerplate/react-boilerplate>`_ project where you can find how to use individual libraries included in the project and also the motivation for why to use them. Our application does not strictly follow all the patterns introduced in the boilerplate project.

**************************
 Most important libraries
**************************

- `React <https://reactjs.org/>`_ - UI library
- `Ant Design <https://github.com/ant-design/ant-design>`_ - components for building the UI
- `Redux <https://redux.js.org/>`_ - state management
- `Redux-Saga <https://github.com/redux-saga/redux-saga>`_ - asynchronous data loading
- `React Router <https://github.com/ReactTraining/react-router>`_ - routing
- `React Intl <https://github.com/formatjs/react-intl>`_ - localization

**************************
 Application structure
**************************

The whole application is divided into three different modules:

- *public* - part of the application that is available to all the users
- *admin* - part of the appliation that is available only to organizers and admin
- *shared* - everything that is shared between the two modules

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
==========================

In the React ecosystem, we often distinguish between *(presentational) components* and *containers*. *Components* are concerned with *how things look*, while *containers*

.. todo:: TODO

Ducks
==========================

Pages
==========================

**************************
API resources
**************************

Throughout the whole application, it is needed to send requests to the API server and do something with the response. The application therefore containss abstractions to make the communication with API server easier for developers.

CRUD
==========================

The most common operations on API resources are CRUD operations (create, read, update, delete). There is a ``resourceFactory`` function which provides basic functionality to handle CRUD operations. The resource is created like this (most often in the *<module>/ducks/resourceName.js* file):

.. code-block:: js

  export const { actions, actionTypes, reducers, selectors } = resourceFactory({
    endpoint: 'api/documents',
    resourceName: 'documents',
  });


Actions
--------------------------

Actions can be dispatched to communicate with the api server. If there is some response from the server, it is stored in the redux store.

*Currently available actions:*

- ``fetchMany(queryParams)``
- ``fetchResource(id)``
- ``updateResource(id, data)``
- ``createResource(data)``
- ``deleteResource(id)``

*Under the hood* (e.g. after *fetchMany* function is called):

- ``CALL_API`` action is dispatched
- saga is called when such action is dispatched
- saga dispatches ``FETCH_MANY_REQUEST`` action to signal start of the request
- saga creates an api request based on the action payload
- on success, ``FETCH_MANY_SUCCESS`` action is dispatched with response data
- on failure, ``FETCH_MANY_FAILURE`` action is dispatched with response data

Action types
--------------------------

Exported action types can be used to hook into individual stages of api requests. For example, if we want to redirect the user to the detail page after we create a resource, we can do so if we react to the ``actionTypes.CREATE_SUCCESS`` action.

*Action types suffixes*:

- ``REQUEST``
- ``SUCCESS``
- ``FAILURE``

*Currently available action types*:

- ``FETCH_${SUFFIX}``
- ``FETCH_MANY_${SUFFIX}``
- ``CREATE_${SUFFIX}``
- ``UPDATE_${SUFFIX}``
- ``DELETE_${SUFFIX}``

Reducers
--------------------------

Exported reducers handle actions with the action types above. For example, on ``FETCH_MANY_REQUEST``, the ``isFetching`` flag for the given resource is set to ``true``. And then, on ``FETCH_MANY_SUCCESS``, the ``isFetching`` flag for the given resource is set to ``false`` and the ``items`` property is filled with the response from the server.

Reducers must be manually registered in the redux store for everything to work correctly.

Selectors
--------------------------

Basic selectors are available to make querying the data easier.

*Currently available selectors*:

- ``getItems()``
- ``getTotalItems()``
- ``getItem()``
- ``getFetchItemError()``
- ``isFetching()``
- ``isFetchingItem()``
- ``isCreating()``
- ``isDeleting()``

Calling API directly
==========================

Not every communication with the API server is one of the CRUD operations. For example, if we want to reset the password of a user, we want to send a ``POST`` request to the ``api/users/passwordReset`` endpoint and that is the only thing we want to do with that endpoint.

In these situations, we call the API directly using the ``callApi`` function. The code structure is often as follows:

.. code-block:: js

  yield put(/* request action*/);

  const { data, status } = yield call(callApi, {
    endpoint: 'api/some/endpoint',
    method: 'POST',
    data: /* data to send */,
  });

  /* check if successful */
  if (status >= 200 && status < 300) {
    yield put(/* success action*/);
    /* do something with the response if needed */
  } else {
    yield put(/* failure action*/);
    /* do something with the response if needed */
  }

**************************
 Localization
**************************

Localization is done using the `React Intl <https://github.com/formatjs/react-intl>`_ library. No text that is visible to the users should be hardoceded in the source code. The basic component for localization is the ``FormattedMessage`` component that takes the id of the message that should be translated:

.. code-block:: js

  <FormattedMessage id="app.public.registrationForm.username" />

The id of the message should somehow correspond to where is the translation used.

Translation
=========================

After we use a FormattedMessage with a new id, the localization plugin does not have any translation available so it always displays the id. To add a translation, we have to first run the ``npm extract-intl`` script. This script goes through all our components and finds all messages that needs to be translated. The output of the script are several files in the app/translations directory. Each of these files corresponds to one language mutation of the website. This is the place where we provide translations for all messages.

.. code-block:: json

    {
        "app.public.registrationForm.confirmPassword": "Potvrdit heslo",
        "app.public.registrationForm.email": "Email",
        "app.public.registrationForm.password": "Heslo",
        "app.public.registrationForm.register": "Registrovat",
        "app.public.registrationForm.username": "Uživatelské jméno"
    }

What if we can't use FormattedMessage?
======================================

There are some situations where we can't use the FormattedMessage component:

- FormattedMessage returns a React component but we sometimes need to get a string (e.g. Input placeholder)
- Sometimes we need to use different messages based on some dynamic conditions, but with FormattedMessage we need a constant id

For such situations, we can use the lower level api:

- if we need to translate something in a component, create a *localization.js* file next to the component
- define translatable messages like below:


.. code-block:: js

  import { defineMessages } from 'react-intl';

  export const intlMessages = defineMessages({
    title: { id: 'app.registrationForm.title' },
    username: { id: 'app.registrationForm.username' },
  });


- import messages together with the *intl* object:

.. code-block:: js

  import { intl } from '@/modules/shared/helpers/IntlGlobalProvider';
  import { intlMessages } from 'path/to/localization.js';

- get translated messages:

.. code-block:: js

  <Input placeholder={intl.formatMessage(intlMessages.username)} />
