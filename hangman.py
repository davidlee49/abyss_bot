
import discord.ui
import random


class HangmanBoard(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.hits = 5
        self.word = self.get_word()
        self.word_set = set(self.word)
        self.found_letters = "-" * len(self.word)

    def get_word(self):
        words = ["HELLO", "GOODBYE", "PEACHES", "TOMAHAWK", "PEPPER", "ARRANGE", "DISORDER", "COLLECT", "DOLL",
                 "WITNESS", "LAKE", "WORM", "HESITATE", "FORWARD", "COMPLAIN"]
        word = words[random.randint(0, len(words)-1)]
        return word

    def check_guess_and_update(self, letter, button):
        button.disabled = True
        if letter in self.word_set:
            update_word = ""
            for index, char in enumerate(self.word):
                if letter == char or self.found_letters[index] == char:
                    update_word += char
                else:
                    update_word += "-"
            self.found_letters = update_word
            return True
        else:
            self.hits -= 1
            return False

    def disable_buttons(self):
        for all_buttons in self.children:
            all_buttons.disabled = True

    @discord.ui.button(label="A")
    async def a_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="E")
    async def e_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="I")
    async def i_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="O")
    async def o_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="U")
    async def u_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="B")
    async def b_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="C")
    async def c_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="D")
    async def d_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="F")
    async def f_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="G")
    async def g_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="H")
    async def h_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="J")
    async def j_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="K")
    async def k_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="L")
    async def l_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="M")
    async def m_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="N")
    async def n_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="P")
    async def p_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="Q")
    async def q_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="R")
    async def r_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="S")
    async def s_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="T")
    async def t_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="V")
    async def v_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="W")
    async def w_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="Y")
    async def y_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)

    @discord.ui.button(label="Z")
    async def z_cb(self, interaction, button):
        if self.check_guess_and_update(button.label, button) is False and self.hits == 0:
            self.disable_buttons()
            await interaction.response.edit_message(content=f"You Lose! The word was {self.word}", view=self)
        elif self.found_letters == "".join(self.word):
            self.disable_buttons()
            await interaction.response.edit_message(content="You Win!", view=self)
        else:
            await interaction.response.edit_message(
                content=f"You have {self.hits} left! Current word: {self.found_letters}", view=self)
