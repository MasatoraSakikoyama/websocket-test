/* globals Vue, Vuex */
import template from 'components/components.html';
import 'components/components.css';
import AppHeader from 'components/header/header';
import AppContents from 'components/contents/contents';
import AppFooter from 'components/footer/footer';
import Menu from 'components/menu/menu';
import modalFactory from 'components/common/modal/modal.factory';
import { SESSION, IS_LOGIN } from 'store/modules/session/types';
import * as info from 'store/modules/info/types';
import * as error from 'store/modules/error/types';

export default Vue.extend({
  template,
  computed: {
    ...Vuex.mapState(SESSION, {
      isLogin: IS_LOGIN,
    }),
  },
  components: {
    'app-header': AppHeader,
    'app-contents': AppContents,
    'app-footer': AppFooter,
    'app-menu': Menu,
    'info-modal': modalFactory(info.INFO, info),
    'error-modal': modalFactory(error.ERROR, error),
  },
});
