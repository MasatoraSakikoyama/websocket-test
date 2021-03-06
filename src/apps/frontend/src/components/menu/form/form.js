/* globals Vue, Vuex */
import jwt from 'utils/jwt.axios';
import template from 'components/menu/form/form.html';
import 'components/menu/form/form.css';
import factory from 'components/common/input/component.factory';
import { ERROR, OPEN_MODAL } from 'store/modules/error/types';

export default Vue.extend({
  template,
  data() {
    return {
      model: {
        key: 'Title',
        value: null,
        isValid: false,
        rules: [
          { name: 'NotEmpty' },
          { name: 'MaxLength', param: 255 },
        ],
      },
    };
  },
  components: {
    'text-input': factory('text'),
  },
  methods: {
    ...Vuex.mapActions(ERROR, {
      openModal: OPEN_MODAL,
    }),
    onCreateRoom() {
      if (!this.model.isValid) {
        return;
      }
      jwt.post('/api/room/create', {
        title: this.model.value,
        password: null,
        is_private: false,
        is_anonymous: true,
      })
      .then((response) => {
        this.model.value = null;
        this.$emit('create-room', response.data);
        this.$router.push({
          name: 'chat',
          params: { roomId: response.data.room_id },
        });
      })
      .catch(() => {
        this.openModal({
          title: 'Room',
          message: 'Fail create',
        });
      });
    },
  },
});
