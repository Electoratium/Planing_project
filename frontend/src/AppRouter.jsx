import React, { Component, Fragment } from 'react';
import PropTypes from 'prop-types';
import ImmutablePropTypes from 'react-immutable-proptypes';
import { connect } from 'react-redux';
import { Redirect } from 'react-router';
import { Router, Route, Switch } from 'react-router-dom';
import { bindActionCreators } from 'redux';
import PrivateRoute from './containers/PrivateRoute';
import Drawer from './components/base/Drawer';
import Footer from './components/base/Footer';
import Home from './components/pages/Home';
import Login from './components/pages/Login';
import SignUp from './components/pages/SignUp';
import SnackBar from './components/SnackBar';
import Day from './containers/pages/planing/Day';
import Week from './containers/pages/planing/Week';
import Month from './containers/pages/planing/Month';
import Year from './containers/pages/planing/Year';
import Projects from './containers/pages/planing/Projects';
import NotFound from './components/pages/NotFound';
import loginActions from './actions/auth';
import history from './history/history';



/*
  TO DO: YOU HAVE TO CHANGE PROPS.TYPE WHICH ARE GETTING FROM STORE TO ImmutablePropTypes.map.isRequired
   and change getting this properties because it getting not object or arr -> map or list (use get);
*/
class AppRouter extends Component {
	constructor (props) {
		super(props);

		const { onCheckToken } = this.props;

		onCheckToken();
	}

	showDangerBar() {
		const { login } = this.props;

		if (login.get('error')) {
			return (
				<SnackBar
					message={login.get('error')}
				/>
			);
		}
	}

	render() {
		return (
			<Router history={history}>
				<Fragment>
					{ this.showDangerBar()}
					<Drawer>
						<Switch>
							<Route path="/" exact component={Home} />

							<PrivateRoute
								exact
								path="/planing"
								component={
									<Redirect to="/planing/day" />
								}
							/>
							<PrivateRoute path="/planing/day" component={Day} />
							<PrivateRoute path="/planing/week" component={Week} />
							<PrivateRoute path="/planing/month" component={Month} />
							<PrivateRoute path="/planing/year" component={Year} />
							<PrivateRoute path="/planing/projects" component={Projects} />

							<Route path="/login" component={Login} />
							<Route path="/sign-up" component={SignUp} />

							<Route component={NotFound} />
						</Switch>
					</Drawer>

					{/* <Footer /> */}
				</Fragment>
			</Router>
		);
	}
}


AppRouter.propTypes = {
	onCheckToken: PropTypes.func.isRequired,
	// login: PropTypes.object.isRequired,
	login: ImmutablePropTypes.map.isRequired
};

function mapStateToProps(state) {
	return {
		login: state.login,
	};
}

function matchDispatchToProps(dispatch) {
	return bindActionCreators({
		onCheckToken: () => loginActions.checkToken(),
	}, dispatch);
}

export default connect(
	mapStateToProps,
	matchDispatchToProps,
)(AppRouter);
