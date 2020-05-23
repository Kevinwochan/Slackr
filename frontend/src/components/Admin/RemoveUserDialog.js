import React from "react";
import axios from 'axios';
import {
  Dialog,
  DialogTitle,
  DialogActions,
  DialogContent,
  DialogContentText,
  Button,
  TextField,
  Grid,
  FormControlLabel,
  RadioGroup,
  Radio,
  MenuItem,
  Select,
  InputLabel,
} from "@material-ui/core";
import AuthContext from "../../AuthContext";
import { PERMISSION_IDS } from "../../utils/constants";

export default function RemoveUserDialog({ children, ...props }) {

    const [open, setOpen] = React.useState(false);
    const [permissionId, setPermissionId] = React.useState(PERMISSION_IDS.MEMBER);
    const [users, setUsers] = React.useState([]);
    const [selectedUser, setSelectedUser] = React.useState('');
    const token = React.useContext(AuthContext);

    function fetchUserData() {
    axios
      .get('/users/all', {
        params: {
          token,
        },
      })
      .then(({ data }) => {
        setUsers(data['users']);
      })
      .catch((err) => {});
     }

    React.useEffect(() => {
        fetchUserData();
    }, []);


    const handleRadioChange = event => {
        const newPermissionId = parseInt(event.target.value,10);
        setPermissionId(newPermissionId);
    };

    const handleUserSelect = event => {
        const newUserId = parseInt(event.target.value,10);
        setSelectedUser(newUserId);
    };

    function handleClickOpen() {
        setOpen(true);
    }

    function handleClose() {
        setOpen(false);
    }

    function handleSubmit(event) {
        event.preventDefault();

        if (!event.target[0].value) return;

        const u_id = parseInt(event.target[0].value,10);
        axios
        .delete(`/admin/user/remove`, { data : {token, u_id }})
        .then(response => {
            console.log(response);
        })
        .catch(err => {});
    }

    return <>
        <div onClick={handleClickOpen}>
        {children}
        </div>
        <Dialog
            open={open}
            onClose={handleClose}
            aria-labelledby="form-dialog-title"
        >
            <DialogTitle id="form-dialog-title">Remove User</DialogTitle>
            <form onSubmit={handleSubmit}>
                <DialogContent>
                    <DialogContentText>
                    Select a user below to remove
                    </DialogContentText>
                    <Grid
                        container
                        spacing={2}
                        direction="row"
                        justify="center"
                        alignItems="center"
                    >
                        <Grid item xs={12}>
                            <Select style={{width:"100%"}} id="u_id" onChange={handleUserSelect} value={selectedUser}>
                              {users.map((d, idx) => {
                                return <MenuItem key={d.u_id} value={d.u_id}>{d.name_first} {d.name_last}</MenuItem>
                              })}
                            </Select>
                        </Grid>
                    </Grid>
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose} color="primary">
                    Cancel
                    </Button>
                    <Button onClick={handleClose} type="submit" color="primary">
                    Remove
                    </Button>
                </DialogActions>
            </form>
        </Dialog>
    </>;
}
