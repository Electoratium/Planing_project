import Axios from 'axios';
import history from '../history/history';
import constants from '../modules/constants';
import { cookies } from '../modules/manageCookies';
import createData from '../utils/createData';

export const FETCH_DAY = 'FETCH_DAY';
export const SOME_DAY = 'sasddsfdsfdf';

const dayListLoaded = rows => ({
  type: constants.plainningStatus.dayLoaded,
  payload: rows,
});

const dayListTestArray = () => {
  const dayPlanning = [
    createData('Frozen yoghurt', 159, 6.0),
    createData('Ice cream sandwich', 237, 9.0),
    createData('Eclair', 262, 16.0),
    createData('Cupcake', 305, 3.7),
    createData('Gingerbread', 356, 16.0),
    createData('Gingerbread', 356, 16.0),
    createData('Gingerbread', 356, 16.0),
  ];
  return dayPlanning;
};

export const fetchDay = () => (dispatch) => {
  const rows = dayListTestArray();
  dispatch(dayListLoaded(rows));

  // const token = cookies.get('token');
  // console.log('dddd');
  // return Axios.get(`${constants.baseApiUrl}/planing/day`, {
  //   headers: { Authorization: `Token ${token}` },
  // })
  //   .then((response) => {
  //     dispatch({
  //       type: FETCH_DAY,
  //       payload: {
  //         test: 'test',
  //       },
  //     });
  //   })
  //   .catch((err) => {
  //     console.log(err);
  //   });
  //
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
