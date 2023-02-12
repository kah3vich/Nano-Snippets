import * as vscode from 'vscode';

export const activate = (context: vscode.ExtensionContext) => {
	const disposable = vscode.commands.registerCommand('nano-snippets', function () {
		console.log('Nano Snippets');

		context.subscriptions.push(disposable);
	});
};

export const deactivate = () => {};
