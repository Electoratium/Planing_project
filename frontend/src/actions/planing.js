import Axios from 'axios';
import history from '../history/history';
import constants from "../modules/constants";
import {cookies} from "../modules/manageCookies";


export const FETCH_DAY = 'FETCH_DAY';
export const SOME_DAY = 'sasddsfdsfdf';


export const fetchDay = () => (dispatch) => {
	const token = cookies.get('token');

	console.log('dddd');


	return Axios.get(`${constants.baseApiUrl}/planing/day`, { headers: { Authorization: `Token ${token}`}})
		.then((response) => {
			dispatch({
			  type: FETCH_DAY,
			  payload: {
			    'test': 'test'
			  },
			});
		})
		.catch( (err) => {
			console.log(err);
		})

      // .catch((err) => {
      //   if (err.response) {
      //     if (err.response.status === 404) {
      //       return dispatch({
      //         type: constants.loginActions.loginError,
      //         payload: {
      //           errorText: constants.loginErrors.invalidData,
      //         },
      //       });
      //     }
      //   }
      //   dispatch({
      //     type: constants.loginActions.loginError,
      //     payload: {
      //       errorText: constants.loginErrors.serverError,
      //     },
      //   });
      // });
};