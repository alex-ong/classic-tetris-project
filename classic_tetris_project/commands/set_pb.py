from .command import Command, CommandException, register_command

@register_command("newpb", "setpb")
class SetPBCommand(Command):
    usage = "setpb <pb> [type] (default type NTSC)"

    def execute(self, pb, pb_type="ntsc"):
        try:
            pb = int(pb.replace(",", ""))
        except ValueError:
            raise CommandException(send_usage=True)

        pb_type = pb_type.lower()

        if pb < 0:
            self.send_message("Invalid PB.")
        elif pb > 1400000:
            self.send_message("You wish, kid >.>")
        else:
            if self.context.user.set_pb(pb, pb_type):
                self.send_message("{user_tag} has a new {pb_type} pb of {pb:,}!".format(
                    user_tag=self.context.user_tag,
                    pb_type=pb_type.upper(),
                    pb=pb
                ))
            else:
                self.send_message("Invalid PB type - must be NTSC or PAL (default NTSC)")